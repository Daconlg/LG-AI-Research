def worker(param):
    data = param[0]
    smote = param[1]
    train_x, train_y = smote.fit_sample(data['train_x'], data['train_y'])
    data['train_x'] = train_x
    data['train_y'] = train_y
    return data


def worker2(_worker_params):
    func_str = _worker_params[0]
    worker_params = _worker_params[1]
    evec(func_str)