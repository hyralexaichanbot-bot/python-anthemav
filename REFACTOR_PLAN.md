# Python-Anthemav Model Extraction Refactor

**Goal:** Extract model-specific logic from `protocol.py` into separate model classes to improve maintainability and reduce conditional complexity.

**Branch Strategy:**
- Base: `master` (current upstream)
- Each phase creates a feature branch from the previous phase
- PR each phase to the previous feature branch for review
- Final PR merges all phases to `master`

---

## Phase 1: Extract Model Metadata Constants

**Branch:** `feature/model-extraction-phase1`

**Tasks:**
- [ ] Create `anthemav/models/` directory structure
- [ ] Create `anthemav/models/base.py` with `BaseModel` abstract class
- [ ] Create `anthemav/models/x20.py` with X20Model class
- [ ] Create `anthemav/models/x40.py` with X40Model class
- [ ] Create `anthemav/models/mdx.py` with MDXModel class
- [ ] Move constants from `protocol.py` to model classes:
  - `ALM_NUMBER_x20`, `ALM_NUMBER_x40`
  - `COMMANDS_X20`, `COMMANDS_X40`, `COMMANDS_MDX_IGNORE`
  - `ALM_RESTRICTED`, `ALM_RESTRICTED_MODEL`
  - `LOOKUP` and `ZONELOOKUP` (model-specific subsets)
- [ ] Create `anthemav/models/__init__.py` with model registry
- [ ] Update `protocol.py` to use model objects instead of `_model_series` checks for metadata
- [ ] Add tests for model metadata
- [ ] Test with HA: verify integration loads and amplifier control works
- [ ] Create PR to `master`

**Success Criteria:**
- All existing tests pass
- HA integration loads without errors
- Can turn amplifier on/off
- No logic changes, only moving constants

---

## Phase 2: Extract Zone Detection Logic

**Branch:** `feature/model-extraction-phase2` (from phase1)

**Tasks:**
- [ ] Add `get_zone_count(model_name)` to `BaseModel`
- [ ] Implement zone count logic in each model class
- [ ] Add `get_available_input_numbers(model_name)` to `BaseModel`
- [ ] Move `set_zones()` logic from `protocol.py` to model classes
- [ ] Update `protocol.py` to call model methods
- [ ] Add tests for zone detection
- [ ] Test with HA: verify zones work correctly
- [ ] Create PR to `feature/model-extraction-phase1`

**Success Criteria:**
- Zone detection works for x20, x40, and MDX models
- All tests pass
- HA integration works with zones

---

## Phase 3: Extract Command Formatting Logic

**Branch:** `feature/model-extraction-phase3` (from phase2)

**Tasks:**
- [ ] Add `get_commands_to_query()` to `BaseModel`
- [ ] Add `get_commands_to_ignore()` to `BaseModel`
- [ ] Move `set_model_command()` logic to model classes
- [ ] Extract model-specific command handling from `protocol.py`
- [ ] Update `protocol.py` to use model methods for command decisions
- [ ] Add tests for command formatting
- [ ] Test with HA: verify all commands work
- [ ] Create PR to `feature/model-extraction-phase2`

**Success Criteria:**
- Commands are correctly formatted per model
- No regression in existing functionality
- All tests pass

---

## Phase 4: Extract Input Population Logic

**Branch:** `feature/model-extraction-phase4` (from phase3)

**Tasks:**
- [ ] Add `get_input_query_format()` to `BaseModel`
- [ ] Move `_populate_inputs()` model differences to model classes
- [ ] Extract input name parsing logic differences
- [ ] Update `protocol.py` to use model methods
- [ ] Add tests for input population
- [ ] Test with HA: verify input switching works
- [ ] Create PR to `feature/model-extraction-phase3`

**Success Criteria:**
- Input names populate correctly for all models
- Input switching works in HA
- All tests pass

---

## Phase 5: Cleanup and Consolidation

**Branch:** `feature/model-extraction-phase5` (from phase4)

**Tasks:**
- [ ] Remove deprecated `_model_series` attribute from `protocol.py`
- [ ] Remove unused constants from `protocol.py`
- [ ] Update documentation
- [ ] Final integration test with HA
- [ ] Create final PR to merge all phases to `master`
- [ ] Update version to 1.6.0

**Success Criteria:**
- Clean `protocol.py` with minimal model-specific logic
- All tests pass
- HA integration fully functional
- Documentation updated

---

## Current Status

**Active Phase:** Phase 3 - Cleanup and consolidation
**Current Branch:** `feature/model-extraction-phase3`
**Last Completed:** Phase 1 & 2
**Next Action:** Final cleanup, documentation, prepare for merge

## Completed Summary

### Phase 1 ✅
- Created model classes (base.py, x20.py, x40.py, mdx.py)
- Created ModelRegistry with detect_model()
- Updated protocol.py to use model objects
- Branch: feature/model-extraction-phase1

### Phase 2 ✅
- Fixed all tests (45 passing)
- Wired set_zones() to model
- HA integration tested with MRX 520
- Branch: feature/model-extraction-phase2

### Phase 3 (In Progress)
- Final cleanup
- Documentation updates
- Prepare merge strategy

## Notes

- Test with MRX 520 at 192.168.1.43:14999 after each phase
- HA config: `/home/azureuser/dev/homeassistant-core/config`
- HA venv: `/home/azureuser/dev/homeassistant-core/venv`
- python-anthemav installed in editable mode in HA venv

## Blockers

None currently.

---

*Last updated: 2026-03-04*
