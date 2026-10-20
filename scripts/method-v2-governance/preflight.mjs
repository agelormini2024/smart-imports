#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {phaseMode, evaluatePreflight} from './core.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const policy = JSON.parse(fs.readFileSync(path.join(here, 'policy.json'), 'utf8'));
const manifest = JSON.parse(fs.readFileSync(path.join(here, 'candidates', 'brand-cand-009.json'), 'utf8'));
const repo = path.join(os.homedir(), 'Desktop', 'smart-imports');
const git = (...args) => execFileSync('git', args, {cwd:repo, encoding:'utf8', stdio:['ignore','pipe','pipe']}).trim();
const safe = (fn, fallback = false) => {try{return fn();}catch{return fallback;}};
const rpath = rel => path.join(repo,rel);
const exists = rel => fs.existsSync(rpath(rel));
const content = rel => exists(rel) ? fs.readFileSync(rpath(rel),'utf8') : '';
const sha = filename => crypto.createHash('sha256').update(fs.readFileSync(filename)).digest('hex');
const cwd = path.join(os.homedir(),'Desktop');
const baselinePath = path.join(cwd, manifest.lastValidated.matrixDesktopRelative);
const logPath = path.join(cwd, manifest.lastValidated.logDesktopRelative);
const log = fs.existsSync(logPath) ? fs.readFileSync(logPath,'utf8') : '';
const roadmap = content(manifest.roadmapPath);
const candidate = content(manifest.candidatePath);
const contract = content(manifest.contractPath);
const origin = safe(() => git('rev-parse','origin/main'), 'NONE');
const head = safe(() => git('rev-parse','HEAD'), 'NONE');
const status = safe(() => git('status','--porcelain','--untracked-files=all').split('\n').filter(Boolean), ['UNAVAILABLE']);
const unexpected = status.filter(row => !(row.startsWith('?? ') && row.slice(3).startsWith('.update-backups/')));
const marker = phase => `<!-- BRAND-CAND-009-${phase}-DOCUMENTARY-CHECKPOINT:START -->`;
const inBoth = phase => roadmap.includes(marker(phase)) && candidate.includes(marker(phase));
const tracked = rel => exists(rel) && safe(() => {git('ls-files','--error-unmatch','--',rel); return true;});
const shaMatch = fs.existsSync(baselinePath) && sha(baselinePath) === manifest.lastValidated.sha256;
const passes = /Phase:\s*F7\b/.test(log) && /1\/2\s*[—-]\s*Data Fidelity Preflight/.test(log) && /2\/2\s*[—-]\s*Matrix Validator/.test(log) && /RESULT:\s*PASS/.test(log) && /"result":\s*"PASS"/.test(log) && /CHECKPOINT:\s*PASS\s*[—-]\s*DATA FIDELITY \+ MATRIX VALIDATOR/.test(log) && log.includes(manifest.lastValidated.sha256) && /"errors":\s*0/.test(log) && /"warnings":\s*0/.test(log);
const ctx = {
  candidateValid: manifest.candidate === 'BRAND-CAND-009' && manifest.f8FounderApproval === 'NOT_REQUESTED',
  nextPhase: manifest.nextPhase,
  phaseMode: phaseMode(policy, manifest.nextPhase),
  repoOnMain: safe(() => git('branch','--show-current') === 'main'),
  gitSynchronized: head !== 'NONE' && origin !== 'NONE' && head === origin,
  publishedCommitAncestor: safe(() => {git('merge-base','--is-ancestor', manifest.publishedCommitAtPreflightCreation, 'HEAD'); return true;}),
  repoClean: unexpected.length === 0,
  contractApproved: /(^|\n)status:\s*approved\s*(\n|$)/.test(contract),
  contractVersion: /(^|\n)version:\s*1\.0\.7\s*(\n|$)/.test(contract),
  cadencePresent: contract.includes('METHOD-V2-GOVERNANCE-CADENCE:START') && contract.includes('F4–F6') && contract.includes('F7–F8'),
  baselineHashMatches: shaMatch,
  f7LogDualPass: passes,
  f03Published: inBoth('F0-F3'),
  f46Published: inBoth('F4-F6'),
  researchTracked: manifest.researchPublished.every(tracked),
  f7Reserved: !tracked(manifest.researchReservedForNextBlock) && candidate.includes('F7 TECHNICALLY CLOSED'),
  f8NotOpened: !/F8\s*(?:[:—-]|\s)\s*OPENED\b/i.test(candidate),
  f14NotOpened: manifest.f14 === 'NOT_OPENED' && !/F14\s*(?:[:—-]|\s)\s*OPENED\b/i.test(candidate)
};
const result = evaluatePreflight(ctx);
console.log('SMART IMPORTS — METHOD V2 GOVERNANCE PREFLIGHT v0.2.0');
console.log(`Repo: ${repo}`);
console.log(`HEAD: ${head}`);
console.log(`origin/main local: ${origin}`);
console.log('No se ejecuta git fetch: la sincronización es de referencias locales, no consulta remota.');
console.log(`Matriz F7 SHA: ${shaMatch ? 'PASS' : 'FAIL'}`);
console.log(`Cambios Git inesperados: ${unexpected.length ? JSON.stringify(unexpected) : 'ninguno'}`);
for(const check of result.checks) console.log(`[${check.status}] ${check.id} — ${check.explanation}`);
console.log(`RESULTADO: ${result.verdict}`);
console.log('Esta validación no reemplaza el análisis factual, el doble PASS ni la aprobación expresa del Founder al cerrar F8.');
process.exitCode = result.verdict === 'BLOCKED' ? 2 : 0;
