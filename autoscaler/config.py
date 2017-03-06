import os

import envparse

env = envparse.Env()

class Config(object):
    CAPACITY_DATA = os.environ.get('CAPACITY_DATA', 'data/capacity.json')
    CAPACITY_CPU_RESERVE = float(os.environ.get('CAPACITY_CPU_RESERVE', 0.0))
    ENABLED_GRACE_PERIODS = {
        'LAUNCH_HOUR_OFFSET': env('AUTOSCALER_GRACE_PERIOD_LAUNCH_HOUR_OFFSET_ENABLED', cast=bool, default=True)
    }
    TYPE_IDLE_COUNT = env('AUTOSCALER_CLUSTER_TYPE_IDLE_COUNT', cast=int, default=5)
    UTILISATION_THRESHOLD = env('AUTOSCALER_CLUSTER_UTILISATION_THRESHOLD', cast=float, default=0.3)
    DRAIN_GRACE_PERIOD_SECONDS = env('AUTOSCALER_KUBE_POD_DRAIN_GRACE_PERIOD_SECONDS', cast=int, default=300)
