# sample tuners
from btb.tuning import Uniform as UniformTuner, GP, GPEi, GPEiVelocity
# hyperpartition selectors
from btb.selection import Uniform as UniformSelector, UCB1,\
                          BestKReward, BestKVelocity, RecentKReward,\
                          RecentKVelocity, HierarchicalByAlgorithm,\
                          PureBestKVelocity

# A bunch of constants which are used throughout the project, mostly for config.
# TODO: convert these lists and classes to something more elegant, like enums
SQL_DIALECTS = ['sqlite', 'mysql']
SCORE_TARGETS = ['cv', 'test', 'mu_sigma']
BUDGET_TYPES = ['none', 'classifier', 'walltime']
METHODS = ['logreg', 'svm', 'sgd', 'dt', 'et', 'rf', 'gnb', 'mnb', 'bnb',
           'gp', 'pa', 'knn', 'mlp', 'ada']
TUNERS = ['uniform', 'gp', 'gp_ei', 'gp_eivel']
SELECTORS = ['uniform', 'ucb1', 'bestk', 'bestkvel', 'purebestkvel', 'recentk',
             'recentkvel', 'hieralg']
DATARUN_STATUS = ['pending', 'running', 'complete']
CLASSIFIER_STATUS = ['running', 'errored', 'complete']
PARTITION_STATUS = ['incomplete', 'errored', 'gridding_done']

TIME_FMT = "%Y-%m-%d %H:%M"
DATA_PATH = 'data/downloads'

TUNERS_MAP = {
    'uniform': UniformTuner,
    'gp': GP,
    'gp_ei': GPEi,
    'gp_eivel': GPEiVelocity,
}

SELECTORS_MAP = {
    'uniform': UniformSelector,
    'ucb1': UCB1,
    'bestk': BestKReward,
    'bestkvel': BestKVelocity,
    'purebestkvel': PureBestKVelocity,
    'recentk': RecentKReward,
    'recentkvel': RecentKVelocity,
    'hieralg': HierarchicalByAlgorithm,
}

METHODS_MAP = {
    'logreg': 'logistic_regression.json',
    'svm': 'support_vector_machine.json',
    'sgd': 'stochastic_gradient_descent.json',
    'dt': 'decision_tree.json',
    'et': 'extra_trees.json',
    'rf': 'random_forest.json',
    'gnb': 'gaussian_naive_bayes.json',
    'mnb': 'multinomial_naive_bayes.json',
    'bnb': 'bernoulli_naive_bayes.json',
    'gp': 'gaussian_process.json',
    'pa': 'passive_aggressive.json',
    'knn': 'k_nearest_neighbors.json',
    'mlp': 'multi_layer_perceptron.json',
    'ada': 'adaboost.json'
}

class ClassifierStatus:
    RUNNING = 'running'
    ERRORED = 'errored'
    COMPLETE = 'complete'

class RunStatus:
    PENDING = 'pending'
    RUNNING = 'running'
    COMPLETE = 'complete'

class PartitionStatus:
    INCOMPLETE = 'incomplete'
    GRIDDING_DONE = 'gridding_done'
    ERRORED = 'errored'

S3_PREFIX = '^s3://'
HTTP_PREFIX = '^https?://'

class FileType:
    LOCAL = 'local'
    S3 = 's3'
    HTTP = 'http'

# these are the strings that are used to index into results dictionaries
class Metrics:
    ACCURACY = 'accuracy'
    RANK_ACCURACY = 'rank_accuracy'
    COHEN_KAPPA = 'cohen_kappa'
    F1 = 'f1'
    F1_MICRO = 'f1_micro'
    F1_MACRO = 'f1_macro'
    ROC_AUC = 'roc_auc'     # receiver operating characteristic
    ROC_AUC_MICRO = 'roc_auc_micro'
    ROC_AUC_MACRO = 'roc_auc_macro'
    AP = 'ap'               # average precision
    MCC = 'mcc'             # matthews correlation coefficient
    PR_CURVE = 'pr_curve'
    ROC_CURVE = 'roc_curve'
    CONFUSION_MATRIX = 'confusion_matrix'

METRICS_BINARY = [
    Metrics.ACCURACY,
    Metrics.COHEN_KAPPA,
    Metrics.F1,
    Metrics.ROC_AUC,
    Metrics.AP,
    Metrics.MCC,
    Metrics.CONFUSION_MATRIX,
]

METRICS_MULTICLASS = [
    Metrics.ACCURACY,
    Metrics.RANK_ACCURACY,
    Metrics.COHEN_KAPPA,
    Metrics.F1_MICRO,
    Metrics.F1_MACRO,
    Metrics.ROC_AUC_MICRO,
    Metrics.ROC_AUC_MACRO,
    Metrics.CONFUSION_MATRIX,
]

METRICS = list(set(METRICS_BINARY + METRICS_MULTICLASS))

N_FOLDS_DEFAULT = 10
