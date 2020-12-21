# -*- coding: utf-8 -*-

# python backdoor_attack.py --attack badnet --verbose --pretrain --validate_interval 1 --epoch 50 --lr 1e-2 --mark_height 3 --mark_width 3 --mark_alpha 0.0

import trojanvision.environ
import trojanvision.datasets
import trojanvision.models
import trojanvision.trainer
import trojanvision.marks
import trojanvision.attacks

from trojanvision.utils import summary
import argparse

import warnings
warnings.filterwarnings("ignore")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    trojanvision.environ.add_argument(parser)
    trojanvision.datasets.add_argument(parser)
    trojanvision.models.add_argument(parser)
    trojanvision.trainer.add_argument(parser)
    trojanvision.marks.add_argument(parser)
    trojanvision.attacks.add_argument(parser)
    args = parser.parse_args()

    env = trojanvision.environ.create(**args.__dict__)
    dataset = trojanvision.datasets.create(**args.__dict__)
    model = trojanvision.models.create(dataset=dataset, **args.__dict__)
    trainer = trojanvision.trainer.create(dataset=dataset, model=model, **args.__dict__)
    mark = trojanvision.marks.create(dataset=dataset, **args.__dict__)
    attack = trojanvision.attacks.create(dataset=dataset, model=model, mark=mark, **args.__dict__)

    if env['verbose']:
        summary(env=env, dataset=dataset, model=model, mark=mark, trainer=trainer, attack=attack)
    attack.attack(**trainer)
