import numpy as np


class risk_model():
    # Class of the risk models
    # including: statistical, fundamental, and macro
    @staticmethod
    def statistical(raw_ret, cov=None, model_type="Statistical", K=7):
        # statistical risk model
        # https://arxiv.org/pdf/1602.08070.pdf
        # K - Number of the principle components
        # Demean:
        if cov is None:
            print("generating covariance from the raw return inputs")
            assert (type(raw_ret) == np.array), "Raw return input has to be np.array"
            ret = raw_ret - raw_ret.mean(axis=0)
            cov = np.cov(ret.T)
        # eigen decomposition derivation:
        # http://fourier.eng.hmc.edu/e176/lectures/algebra/node9.html
        w, v = np.linalg.eig(cov)
        w_index = w.argsort()[::-1]  # from largest to smallest
        w_first_K = w[w_index[:K]]
        v_first_K = v[:, w_index[:K]]
        # V * diag(\lambda) * V.T
        return np.matmul(np.matmul(v_first_K, np.diag(w_first_K)), v_first_K.T)


# a = np.array([[1, 2, 4],
#               [4, 4, 3],
#               [1, 3, 5],
#               [0, 5, 5]])
# a_dm = a - a.mean(axis=0)
# cov = np.cov(a_dm.T)
# r = risk_model()
# print(r.statistical(None, cov, None, 2))
