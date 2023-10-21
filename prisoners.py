import time
import random
import argparse

def random_boxes(prisoners, warehouse):

    boxes = list(warehouse.keys())

    prisoner_ids = list(prisoners.keys())
    random.shuffle(prisoner_ids)

    for pid in prisoner_ids:

        open_boxes = []
        half = round(len(open_boxes) / 2)
        for _ in range(half):
            box_number = random.choice(boxes)
            open_boxes.append(warehouse[box_number])

        for box in open_boxes:
            if warehouse[box] == pid:
                prisoners[pid] = True
                break

    return prisoners


def linked_boxes(prisoners, warehouse):

    prisoner_ids = list(prisoners.keys())
    random.shuffle(prisoner_ids)

    half = round(len(prisoner_ids) / 2)

    for pid in prisoner_ids:

        next_box = pid
        for _ in range(half):

            if warehouse[next_box] == pid:
                prisoners[pid] = True
                break

            next_box = warehouse[next_box]

    return prisoners


def successful(prisoners):

    for pid, success in prisoners.items():
        if not success:
            return False

    return True


def mass_exec(iterations, prisoner_count, test_method):

    results = {'success': 0, 'fail': 0}

    for _ in range(iterations):

        warehouse, prisoners = init_data(prisoner_count)

        prisoner_results = test_method(prisoners, warehouse)
        success = successful(prisoner_results)

        if success:
            results['success'] += 1
        else:
            results['fail'] += 1

    return results


def init_data(prisoner_count):

    boxes = {}
    slips = []
    prisoners = {}

    for i in range(100):

        boxes.setdefault(i, None)
        prisoners.setdefault(i, None)
        slips.append(i)

    random.shuffle(slips)

    warehouse = dict(zip(boxes, slips))

    return warehouse, prisoners


def init_args():

    parser = argparse.ArgumentParser(
            prog='LinkedPrisoners',
            description='Simulates linked prisoner dilemma',
            epilog='https://www.youtube.com/watch?v=iSNsgj1OCLA'
            )

    parser.add_argument('-i', '--iterations', default=1000, help='Number of simulation tests to run', type=int, required=False, dest='iterations', action='store')
    parser.add_argument('-p', '--prisoners', default=100, help='Number of prisoners in each simulation', type=int, required=False, dest='prisoners', action='store')
    parser.add_argument('-s', '--simulation', default='linked', help='Type of simulation', choices=['linked','random'], required=False, dest='simtype', action='store')

    args = parser.parse_args()
    return args


if __name__ == '__main__':

    conf = init_args()

    sim_type = None
    if conf.simtype == 'random':
        sim_type = random_boxes
    elif conf.simtype == 'linked':
        sim_type = linked_boxes

    time.process_time_ns()
    results = mass_exec(
            iterations=conf.iterations,
            prisoner_count=conf.prisoners,
            test_method=sim_type
            )
    duration = round(time.process_time_ns() * 1e-9, 2)

    print(results)
    print('%s %s simulations of %s prisoners in %s seconds' % (conf.iterations, conf.simtype, conf.prisoners, duration))
