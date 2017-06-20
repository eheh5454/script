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
 "���ڿ��� ��Ĩ�ϴ�."},
 {NULL, NULL, 0, NULL} // �迭�� ���� ��Ÿ���ϴ�.
}; 

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",            // ��� �̸�
    "It is test module.", // ��� ������ ���� �κ�, ����� __doc__�� ����˴ϴ�.
    -1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
