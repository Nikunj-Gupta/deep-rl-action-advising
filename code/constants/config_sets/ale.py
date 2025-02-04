# This file constructs configuration sets for easier management
# A predefined option can be run as follows (1000 for Pong with seed 0, for instance):
# bc_base.py --env-key ALE-Pong --config-set 1000 --seed 0


def generate_config():
    config = {0: {}, 1: {}}
    config[0]['run-id'] = None
    config[0]['process-index'] = 0
    config[0]['machine-name'] = 'NONE'
    config[0]['n-training-frames'] = int(5e6)
    config[0]['n-evaluation-trials'] = 10
    config[0]['evaluation-period'] = int(50e3)

    config[1]['visualize-videos'] = True
    config[0]['evaluation-visualization-period'] = 5
    config[0]['visualization-period'] = 50

    config[1]['save-obs-images'] = False

    config[0]['dqn-type'] = 'egreedy'  # 'egreedy', 'noisy'
    config[0]['dqn-gamma'] = 0.99
    config[0]['dqn-rm-type'] = 'uniform'
    config[0]['dqn-rm-init'] = int(50e3)
    config[0]['dqn-rm-max'] = int(500e3)
    config[0]['dqn-per-alpha'] = 0.4
    config[0]['dqn-per-beta'] = 0.6
    config[1]['dqn-per-ims'] = True
    config[0]['dqn-target-update'] = 7500
    config[0]['dqn-batch-size'] = 32
    config[0]['dqn-learning-rate'] = 0.0000625
    config[0]['dqn-train-per-step'] = 1
    config[0]['dqn-train-period'] = 4
    config[0]['dqn-adam-eps'] = 0.00015
    config[0]['dqn-eps-start'] = 1.0
    config[0]['dqn-eps-final'] = 0.01
    config[0]['dqn-eps-steps'] = 250000
    config[0]['dqn-huber-loss-delta'] = 1.0
    config[0]['dqn-n-hidden-layers'] = 1
    config[0]['dqn-hidden-size-1'] = 512
    config[0]['dqn-hidden-size-2'] = 0
    config[1]['dqn-dueling'] = True

    config[1]['dqn-dropout'] = False
    config[0]['dqn-dropout-rate'] = 0.2
    config[0]['dqn-dropout-uc-ensembles'] = int(100)

    config[1]['dump-replay-memory'] = False
    config[1]['use-gpu'] = True
    config[1]['save-models'] = False
    config[0]['model-save-period'] = int(200e3)
    config[0]['env-key'] = 'NONE'
    config[0]['env-training-seed'] = 0
    config[0]['env-evaluation-seed'] = 1
    config[0]['seed'] = 0

    config[1]['load-teacher'] = False
    config[1]['execute-teacher-policy'] = False  # Only for debugging the teacher policy

    # Pre-collected Dataset
    config[1]['load-demonstrations-dataset'] = False
    config[1]['preserve-initial-demonstrations-dataset'] = False

    # Learning from Demonstration
    config[1]['use-lfd-loss'] = False
    config[0]['n-pretraining-iterations'] = 0

    config[0]['dqn-ql-loss-weight'] = 1.0
    config[0]['dqn-lm-loss-weight'] = 0.2
    config[0]['dqn-l2-loss-weight'] = 1e-5
    config[0]['dqn-lm-loss-margin'] = 0.8

    # Collection
    config[0]['advice-collection-method'] = 'none'  # 'none', 'early', 'random', 'uncertainty_based'
    config[0]['advice-collection-budget'] = 0
    config[0]['advice-collection-uncertainty-threshold'] = 0
    config[1]['preserve-collected-advice'] = False  # Always preserve collected advice transitions in replay memory

    # Imitation
    config[0]['advice-imitation-method'] = 'none'  # 'none', 'periodic'
    config[0]['advice-imitation-period-steps'] = 0
    config[0]['advice-imitation-period-samples'] = 0
    config[0]['advice-imitation-training-iterations-init'] = 0
    config[0]['advice-imitation-training-iterations-periodic'] = 0

    config[0]['bc-batch-size'] = 32
    config[0]['bc-learning-rate'] = 0.0001
    config[0]['bc-adam-eps'] = 0.00015
    config[0]['bc-dropout-rate'] = 0.35
    config[0]['bc-hidden-size'] = int(512)
    config[0]['bc-uc-ensembles'] = int(100)

    # Reuse
    config[0]['advice-reuse-method'] = 'none'  # 'none', 'restricted', 'extended'
    config[0]['advice-reuse-probability'] = 0
    config[0]['advice-reuse-uncertainty-threshold'] = 0
    config[1]['advice-reuse-probability-decay'] = False
    config[0]['advice-reuse-probability-decay-begin'] = 0
    config[0]['advice-reuse-probability-decay-end'] = 0
    config[0]['advice-reuse-probability-final'] = 0

    config[1]['autoset-advice-uncertainty-threshold'] = False

    return config


# ======================================================================================================================

ALE_AA_BUDGET = 25000  # To be set according to the experiment preference
CONFIG_SETS = {}

# ----------------------------------------------------------------------------------------------------------------------
# Generate demonstrator (Long training)

id = 0
CONFIG_SETS[id] = generate_config()
CONFIG_SETS[id][0]['dqn-rm-type'] = 'uniform'
CONFIG_SETS[id][1]['save-models'] = True
CONFIG_SETS[id][0]['evaluation-period'] = int(50e3)
CONFIG_SETS[id][0]['n-evaluation-trials'] = 10
CONFIG_SETS[id][0]['n-training-frames'] = int(10e6)

# ----------------------------------------------------------------------------------------------------------------------
# Evaluate teacher (with a single evaluation step)
id = 500
CONFIG_SETS[id] = generate_config()
CONFIG_SETS[id][1]['load-teacher'] = True
CONFIG_SETS[id][1]['execute-teacher-policy'] = True
CONFIG_SETS[id][0]['dqn-rm-init'] = int(1e6)  # Do NOT train the model in this evaluation setup
CONFIG_SETS[id][0]['n-training-frames'] = int(50e3)
CONFIG_SETS[id][1]['visualize-videos'] = True
CONFIG_SETS[id][0]['evaluation-visualization-period'] = 1

# ----------------------------------------------------------------------------------------------------------------------
# NA: No Advising (Training from scratch)

id = 1000
CONFIG_SETS[id] = generate_config()

# ----------------------------------------------------------------------------------------------------------------------
# NA: No Advising (Training from scratch) + Dropout

id = 1010
CONFIG_SETS[id] = generate_config()
CONFIG_SETS[id][1]['dqn-dropout'] = True
CONFIG_SETS[id][0]['dqn-dropout-rate'] = 0.2
CONFIG_SETS[id][0]['dqn-dropout-uc-ensembles'] = int(100)

# ----------------------------------------------------------------------------------------------------------------------
# EA: Early Advising

id = 2000
CONFIG_SETS[id] = generate_config()
CONFIG_SETS[id][1]['load-teacher'] = True
CONFIG_SETS[id][0]['advice-collection-method'] = 'early'
CONFIG_SETS[id][0]['advice-collection-budget'] = int(ALE_AA_BUDGET)

# ----------------------------------------------------------------------------------------------------------------------
# EA: Early Advising + Dropout

id = 2010
CONFIG_SETS[id] = generate_config()
CONFIG_SETS[id][1]['load-teacher'] = True
CONFIG_SETS[id][0]['advice-collection-method'] = 'early'
CONFIG_SETS[id][0]['advice-collection-budget'] = int(ALE_AA_BUDGET)
CONFIG_SETS[id][1]['dqn-dropout'] = True
CONFIG_SETS[id][0]['dqn-dropout-rate'] = 0.2
CONFIG_SETS[id][0]['dqn-dropout-uc-ensembles'] = int(100)

# ----------------------------------------------------------------------------------------------------------------------
# RA: Random Advising

id = 2100
CONFIG_SETS[id] = generate_config()
CONFIG_SETS[id][1]['load-teacher'] = True
CONFIG_SETS[id][0]['advice-collection-method'] = 'random'
CONFIG_SETS[id][0]['advice-collection-budget'] = int(ALE_AA_BUDGET)

# ----------------------------------------------------------------------------------------------------------------------
# AR: Advice Reuse
# Paper: "Action Advising with Advice Imitation in Deep Reinforcement Learning" (https://arxiv.org/abs/2104.08441)

id = 5000
CONFIG_SETS[id] = generate_config()
CONFIG_SETS[id][1]['load-teacher'] = True
CONFIG_SETS[id][0]['advice-collection-method'] = 'early'
CONFIG_SETS[id][0]['advice-collection-uncertainty-threshold'] = 0.01
CONFIG_SETS[id][0]['advice-collection-budget'] = int(ALE_AA_BUDGET)
CONFIG_SETS[id][0]['advice-imitation-method'] = 'periodic'
CONFIG_SETS[id][0]['advice-imitation-period-steps'] = int(1e9)
CONFIG_SETS[id][0]['advice-imitation-period-samples'] = CONFIG_SETS[id][0]['advice-collection-budget']
CONFIG_SETS[id][0]['advice-imitation-training-iterations-init'] = int(200e3)
CONFIG_SETS[id][0]['advice-reuse-method'] = 'restricted'
CONFIG_SETS[id][0]['advice-reuse-probability'] = 0.5
CONFIG_SETS[id][0]['advice-reuse-uncertainty-threshold'] = 0.01

# ----------------------------------------------------------------------------------------------------------------------
# AR+A: AR is enhanced with the automatic threshold tuning technique

id = 6000
CONFIG_SETS[id] = generate_config()
CONFIG_SETS[id][1]['load-teacher'] = True
CONFIG_SETS[id][0]['advice-collection-method'] = 'early'
CONFIG_SETS[id][0]['advice-collection-budget'] = int(ALE_AA_BUDGET)
CONFIG_SETS[id][0]['advice-imitation-method'] = 'periodic'
CONFIG_SETS[id][0]['advice-imitation-period-steps'] = int(1e9)
CONFIG_SETS[id][0]['advice-imitation-period-samples'] = CONFIG_SETS[id][0]['advice-collection-budget']
CONFIG_SETS[id][0]['advice-imitation-training-iterations-init'] = int(200e3)
CONFIG_SETS[id][0]['advice-reuse-method'] = 'restricted'
CONFIG_SETS[id][0]['advice-reuse-probability'] = 0.5
CONFIG_SETS[id][1]['autoset-advice-uncertainty-threshold'] = True

# ----------------------------------------------------------------------------------------------------------------------
# AR+A+E: AR+A is enhanced with the unrestricted reuse procedure

id = 7000
CONFIG_SETS[id] = generate_config()
CONFIG_SETS[id][1]['load-teacher'] = True
CONFIG_SETS[id][0]['advice-collection-method'] = 'early'
CONFIG_SETS[id][0]['advice-collection-budget'] = int(ALE_AA_BUDGET)
CONFIG_SETS[id][0]['advice-imitation-method'] = 'periodic'
CONFIG_SETS[id][0]['advice-imitation-period-steps'] = int(1e9)
CONFIG_SETS[id][0]['advice-imitation-period-samples'] = CONFIG_SETS[id][0]['advice-collection-budget']
CONFIG_SETS[id][0]['advice-imitation-training-iterations-init'] = int(200e3)
CONFIG_SETS[id][0]['advice-reuse-method'] = 'extended'
CONFIG_SETS[id][0]['advice-reuse-probability'] = 0.5
CONFIG_SETS[id][1]['autoset-advice-uncertainty-threshold'] = True
CONFIG_SETS[id][1]['advice-reuse-probability-decay'] = True
CONFIG_SETS[id][0]['advice-reuse-probability-decay-begin'] = int(500e3)
CONFIG_SETS[id][0]['advice-reuse-probability-decay-end'] = int(2000e3)
CONFIG_SETS[id][0]['advice-reuse-probability-final'] = 0.1

# ----------------------------------------------------------------------------------------------------------------------
# AR+A+E: AR+A is enhanced with the unrestricted reuse procedure + Dropout

id = 7010
CONFIG_SETS[id] = generate_config()
CONFIG_SETS[id][1]['load-teacher'] = True
CONFIG_SETS[id][0]['advice-collection-method'] = 'early'
CONFIG_SETS[id][0]['advice-collection-budget'] = int(ALE_AA_BUDGET)
CONFIG_SETS[id][0]['advice-imitation-method'] = 'periodic'
CONFIG_SETS[id][0]['advice-imitation-period-steps'] = int(1e9)
CONFIG_SETS[id][0]['advice-imitation-period-samples'] = CONFIG_SETS[id][0]['advice-collection-budget']
CONFIG_SETS[id][0]['advice-imitation-training-iterations-init'] = int(200e3)
CONFIG_SETS[id][0]['advice-reuse-method'] = 'extended'
CONFIG_SETS[id][0]['advice-reuse-probability'] = 0.5
CONFIG_SETS[id][1]['autoset-advice-uncertainty-threshold'] = True
CONFIG_SETS[id][1]['advice-reuse-probability-decay'] = True
CONFIG_SETS[id][0]['advice-reuse-probability-decay-begin'] = int(500e3)
CONFIG_SETS[id][0]['advice-reuse-probability-decay-end'] = int(2000e3)
CONFIG_SETS[id][0]['advice-reuse-probability-final'] = 0.1
CONFIG_SETS[id][1]['dqn-dropout'] = True
CONFIG_SETS[id][0]['dqn-dropout-rate'] = 0.2
CONFIG_SETS[id][0]['dqn-dropout-uc-ensembles'] = int(100)

# ----------------------------------------------------------------------------------------------------------------------
# AIR: AR+A+E is enhanced with the uncertainty-based advice collection

id = 8000
CONFIG_SETS[id] = generate_config()
CONFIG_SETS[id][1]['load-teacher'] = True
CONFIG_SETS[id][0]['advice-collection-method'] = 'uncertainty_based'
CONFIG_SETS[id][0]['advice-collection-budget'] = int(ALE_AA_BUDGET)
CONFIG_SETS[id][0]['advice-imitation-method'] = 'periodic'
CONFIG_SETS[id][0]['advice-imitation-period-steps'] = int(CONFIG_SETS[id][0]['advice-collection-budget'] * 2)
CONFIG_SETS[id][0]['advice-imitation-period-samples'] = int(CONFIG_SETS[id][0]['advice-collection-budget'] // 10)
CONFIG_SETS[id][0]['advice-imitation-training-iterations-init'] = int(200e3)
CONFIG_SETS[id][0]['advice-imitation-training-iterations-periodic'] = int(50e3)
CONFIG_SETS[id][0]['advice-reuse-method'] = 'extended'
CONFIG_SETS[id][0]['advice-reuse-probability'] = 0.5
CONFIG_SETS[id][1]['autoset-advice-uncertainty-threshold'] = True
CONFIG_SETS[id][1]['advice-reuse-probability-decay'] = True
CONFIG_SETS[id][0]['advice-reuse-probability-decay-begin'] = int(500e3)
CONFIG_SETS[id][0]['advice-reuse-probability-decay-end'] = int(2000e3)
CONFIG_SETS[id][0]['advice-reuse-probability-final'] = 0.1
