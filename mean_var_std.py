import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  newshape = np.array(list).reshape(3,3)

  calculations = {
      'mean': [np.mean(newshape, axis=0).tolist(), np.mean(newshape, axis=1).tolist(), np.mean(newshape).tolist()],
      'variance': [np.var(newshape, axis=0).tolist(), np.var(newshape, axis=1).tolist(), np.var(newshape).tolist()],
      'standard deviation': [np.std(newshape, axis=0).tolist(), np.std(newshape, axis=1).tolist(), np.std(newshape).tolist()],
      'max': [np.max(newshape, axis=0).tolist(), np.max(newshape, axis=1).tolist(), np.max(newshape).tolist()],
      'min': [np.min(newshape, axis=0).tolist(), np.min(newshape, axis=1).tolist(), np.min(newshape).tolist()],
      'sum': [np.sum(newshape, axis=0).tolist(), np.sum(newshape, axis=1).tolist(), np.sum(newshape).tolist()],
  }

  return calculations