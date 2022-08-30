#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints info
 * @p: pointer to the info
 * Return: correct output
 */

void print_python_list_info(PyObject *p)
{
	long int size = Pylist_Size(p);
	int a;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (a = 0; a < size; a++)
		printf("Element %i: %s\n", a, Py_TYPE(obj->ob_item[a])->tp_name);
}
