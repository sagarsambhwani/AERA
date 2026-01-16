from enum import Enum


class StepType(str, Enum):
    TASK_START = "TASK_START"
    PROMPT = "PROMPT"
    MODEL_OUTPUT = "MODEL_OUTPUT"
    TOOL_CALL = "TOOL_CALL"
    TOOL_RESULT = "TOOL_RESULT"
    STATE_UPDATE = "STATE_UPDATE"
    VALIDATION = "VALIDATION"
    RETRY = "RETRY"
    ERROR = "ERROR"
    TASK_END = "TASK_END"


class SignalType(str, Enum):
    # Trace / structural
    TRACE_INCOMPLETE = "TRACE_INCOMPLETE"

    # Specification (F1)
    AMBIGUOUS_TASK = "AMBIGUOUS_TASK"
    CONSTRAINT_VIOLATION = "CONSTRAINT_VIOLATION"
    OBJECTIVE_SHIFT = "OBJECTIVE_SHIFT"

    # Planning (F2)
    MISSING_PLANNED_STEP = "MISSING_PLANNED_STEP"
    INCORRECT_STEP_ORDER = "INCORRECT_STEP_ORDER"
    NO_RECOVERY_STRATEGY = "NO_RECOVERY_STRATEGY"

    # Execution (F3)
    STEP_SKIPPED = "STEP_SKIPPED"
    STATE_INCONSISTENCY = "STATE_INCONSISTENCY"
    RETRY_PATTERN = "RETRY_PATTERN"

    # Tool interaction (F4)
    INVALID_TOOL_CALL = "INVALID_TOOL_CALL"
    TOOL_SCHEMA_MISMATCH = "TOOL_SCHEMA_MISMATCH"
    TOOL_ERROR_IGNORED = "TOOL_ERROR_IGNORED"

    # Reasoning (F5)
    FABRICATED_FACT = "FABRICATED_FACT"
    LOGICAL_INCONSISTENCY = "LOGICAL_INCONSISTENCY"
    SELF_CONTRADICTION = "SELF_CONTRADICTION"

    # Resource / control (F6)
    TOKEN_LIMIT_HIT = "TOKEN_LIMIT_HIT"
    TIMEOUT_TRIGGERED = "TIMEOUT_TRIGGERED"
    COST_GUARD_TRIGGERED = "COST_GUARD_TRIGGERED"


class FailureCode(str, Enum):
    # Success
    F0 = "F0"

    # Specification failures
    F1_1 = "F1.1"
    F1_2 = "F1.2"
    F1_3 = "F1.3"

    # Planning failures
    F2_1 = "F2.1"
    F2_2 = "F2.2"
    F2_3 = "F2.3"

    # Execution failures
    F3_1 = "F3.1"
    F3_2 = "F3.2"
    F3_3 = "F3.3"

    # Tool interaction failures
    F4_1 = "F4.1"
    F4_2 = "F4.2"
    F4_3 = "F4.3"

    # Reasoning failures
    F5_1 = "F5.1"
    F5_2 = "F5.2"
    F5_3 = "F5.3"

    # Resource / control failures
    F6_1 = "F6.1"
    F6_2 = "F6.2"
    F6_3 = "F6.3"


class Severity(str, Enum):
    S1 = "S1"  # Cosmetic
    S2 = "S2"  # Degraded
    S3 = "S3"  # Task failure
    S4 = "S4"  # System risk


class Outcome(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class Attribution(str, Enum):
    DETERMINISTIC = "DETERMINISTIC"
    RULE_BASED = "RULE_BASED"
    LLM_ASSISTED = "LLM_ASSISTED"
    HUMAN_CONFIRMED = "HUMAN_CONFIRMED"


class RunStatus(str, Enum):
    COMPLETED = "COMPLETED"
    ABORTED = "ABORTED"
    INTERRUPTED = "INTERRUPTED"
