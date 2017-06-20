#include "python.h"
#include <string.h>

static PyObject * 

spam_strcat(PyObject *self, PyObject *args)
{
	const char* str1 = NULL;
	const char* str2 = NULL;

	if (!PyArg_ParseTuple(args, "ss", &str1, &str2))
		return NULL;

	int my_strcat = strcat(str1, str2);

	return Py_BuildValue("s", my_strcat);
}

static PyMethodDef SpamMethods[] = {
{"strcat", spam_strcat, METH_VARARGS,
 "문자열을 합칩니다."},
 {NULL, NULL, 0, NULL} // 배열의 끝을 나타냅니다.
}; 

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",            // 모듈 이름
    "It is test module.", // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
    -1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
