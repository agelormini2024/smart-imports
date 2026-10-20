/**
 * Contrato puro de gobernanza Method v2. Sin operaciones I/O.
 * Una verificación PASS no equivale a seguridad, factibilidad ni aprobación comercial.
 */
export function phaseMode(policy, phase) {
  return policy.phaseModes[phase] ?? null;
}
export function documentaryBlocks(policy) {
  return policy.cadence.map(({from, to, checkpointAfter}) => ({from,to,checkpointAfter}));
}
export function evaluatePreflight(ctx) {
  const checks = [];
  const req = (id, condition, explanation) => checks.push({id, status: condition ? 'PASS' : 'FAIL', explanation});
  req('GOV-001', ctx.candidateValid && ctx.nextPhase === 'F8' && ctx.phaseMode === 'COLLABORATIVE', 'Identidad, siguiente fase y modo coherentes con el contrato.');
  req('GOV-002', ctx.repoOnMain && ctx.gitSynchronized && ctx.publishedCommitAncestor, 'Rama main, origin/main local sincronizada y checkpoint publicado en historia Git.');
  req('GOV-003', ctx.repoClean, 'Ningún cambio local pendiente salvo .update-backups/.');
  req('GOV-004', ctx.contractApproved && ctx.contractVersion && ctx.cadencePresent, 'Contrato aprobado, versión esperada y cadencia documental presentes.');
  req('GOV-005', ctx.baselineHashMatches, 'SHA-256 de la última matriz validada coincide con manifest.');
  req('GOV-006', ctx.f7LogDualPass, 'Log F7 acredita los dos PASS canónicos y el mismo SHA.');
  req('GOV-007', ctx.f03Published, 'Checkpoint F0–F3 documentado en expediente y roadmap.');
  req('GOV-008', ctx.f46Published && ctx.researchTracked, 'Checkpoint F4–F6 documentado y tres Research publicados en Git.');
  req('GOV-009', ctx.f7Reserved && ctx.f8NotOpened && ctx.f14NotOpened, 'F7 reservado para F7–F8; F8/F14 no abiertos.');
  return {verdict: checks.every(x => x.status === 'PASS') ? 'READY_TO_OPEN_F8_COLLABORATIVE' : 'BLOCKED', checks};
}
