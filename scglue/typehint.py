r"""
Type hint definitions
"""

import numbers
from typing import Any, Mapping, Optional, TypeVar, Union

import h5py
import numpy as np
import scipy.sparse

try:
    # AnnData ≥ 0.12: public location
    from anndata.io import CSRDataset, CSCDataset
    SparseDataset = Union[CSRDataset, CSCDataset]
except Exception:
    try:
        # AnnData 0.10.x: public (experimental) location
        from anndata.experimental import CSRDataset, CSCDataset
        SparseDataset = Union[CSRDataset, CSCDataset]
    except Exception:
        try:
            # Very old AnnData: private names (best-effort)
            from anndata._core.sparse_dataset import SparseDataset as _SparseDataset
            SparseDataset = _SparseDataset
        except Exception:
            try:
                from anndata._core.sparse_dataset import BaseCompressedSparseDataset as SparseDataset
            except Exception:
                # Last resort: don't crash over a type hint
                class SparseDataset:  # type: ignore[no-redef]
                    pass
# --------------------------------------------------------------------


Array = Union[np.ndarray, scipy.sparse.spmatrix]
BackedArray = Union[h5py.Dataset, SparseDataset]
AnyArray = Union[Array, BackedArray]
ArrayOrScalar = Union[np.ndarray, numbers.Number]
Kws = Optional[Mapping[str, Any]]
RandomState = Optional[Union[np.random.RandomState, int]]

T = TypeVar("T")  # Generic type var
