from moa.shape import calculate_shapes
from moa.dnf import reduce_to_dnf
from moa.onf import reduce_to_onf
from moa.backend import generate_python_source


def compiler(context, backend='python', include_conditions=True, use_numba=False):
    shape_context = calculate_shapes(context)
    dnf_context = reduce_to_dnf(shape_context)
    onf_context = reduce_to_onf(dnf_context, include_conditions=include_conditions)

    if backend == 'python':
        return generate_python_source(onf_context, materialize_scalars=True, use_numba=use_numba)
    else:
        raise ValueError(f'unknown backend {backend}')
