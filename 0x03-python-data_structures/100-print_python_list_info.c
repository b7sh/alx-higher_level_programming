#include <listobject.h>
#include <object.h>
#include <python.h>
void print_python_list_info(PyObject *p)
{
	PyListObject *obj = (PyListObject *)p;
	long int size = PyList_Size(p);
	int index;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated)
	for (index = 0; index < size; index++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i]->tp_name))
	}
}
