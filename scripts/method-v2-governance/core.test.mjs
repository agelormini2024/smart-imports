import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {phaseMode,documentaryBlocks,evaluatePreflight} from './core.mjs';

const dirname = path.dirname(fileURLToPath(import.meta.url));
const policy = JSON.parse(fs.readFileSync(path.join(dirname,'policy.json'),'utf8'));
const ok = {
 candidateValid:true, nextPhase:'F8',phaseMode:'COLLABORATIVE',repoOnMain:true,gitSynchronized:true,publishedCommitAncestor:true,repoClean:true,
 contractApproved:true,contractVersion:true,cadencePresent:true,baselineHashMatches:true,f7LogDualPass:true,
 f03Published:true,f46Published:true,researchTracked:true,f7Reserved:true,f8NotOpened:true,f14NotOpened:true
};
const gate = (x,id) => evaluatePreflight(x).checks.find(c=>c.id === id).status;
const fail = (property,code) => {
 const x={...ok,[property]:false};
 assert.equal(gate(x,code),'FAIL');
 assert.equal(evaluatePreflight(x).verdict,'BLOCKED');
};

test('política F3/F8 colaborativas y F4/F7 AUTO',()=>{
 assert.equal(phaseMode(policy,'F3'),'COLLABORATIVE'); assert.equal(phaseMode(policy,'F8'),'COLLABORATIVE');
 assert.equal(phaseMode(policy,'F4'),'AUTO'); assert.equal(phaseMode(policy,'F7'),'AUTO');
});
test('cadencia exactamente F0–F3, F4–F6, F7–F8, F9–F13',()=>{
 assert.deepEqual(documentaryBlocks(policy).map(x=>x.checkpointAfter),['F3','F6','F8','F13']);
});
test('caso válido permite abrir F8 colaborativa',()=>assert.equal(evaluatePreflight(ok).verdict,'READY_TO_OPEN_F8_COLLABORATIVE'));
test('falla identidad/modo',()=>fail('candidateValid','GOV-001'));
test('falla rama principal',()=>fail('repoOnMain','GOV-002'));
test('falla sincronización Git',()=>fail('gitSynchronized','GOV-002'));
test('falla histórico commit publicado',()=>fail('publishedCommitAncestor','GOV-002'));
test('falla working tree',()=>fail('repoClean','GOV-003'));
test('falla contrato no aprobado',()=>fail('contractApproved','GOV-004'));
test('falla cambio de versión de contrato',()=>fail('contractVersion','GOV-004'));
test('falla cadencia no publicada',()=>fail('cadencePresent','GOV-004'));
test('falla SHA baseline',()=>fail('baselineHashMatches','GOV-005'));
test('falla doble PASS F7',()=>fail('f7LogDualPass','GOV-006'));
test('falla F0–F3 no publicado',()=>fail('f03Published','GOV-007'));
test('falla checkpoint F4–F6 omitido',()=>fail('f46Published','GOV-008'));
test('falla Research F4–F6 ausente',()=>fail('researchTracked','GOV-008'));
test('falla F7 filtrado prematuramente a Git',()=>fail('f7Reserved','GOV-009'));
test('falla F8 abierta prematuramente',()=>fail('f8NotOpened','GOV-009'));
test('falla F14 abierta prematuramente',()=>fail('f14NotOpened','GOV-009'));
