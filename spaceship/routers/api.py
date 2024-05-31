from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/matrix')
async def calculate_matrix_product() -> dict:
    mat_a = np.random.randint(0, 10, (10, 10))
    mat_b = np.random.randint(0, 10, (10, 10))

    mat_a_list = mat_a.tolist()
    mat_b_list = mat_b.tolist()

    mat_product = np.dot(mat_a, mat_b)
    mat_product_list = mat_product.tolist()

    return {
        'matrix_a': mat_a_list,
        'matrix_b': mat_b_list,
        'product': mat_product_list
    }