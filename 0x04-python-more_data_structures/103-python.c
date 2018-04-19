#include <Python.h>

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *holder;

	printf("[.] bytes object info\n");
	if (PyBytes_CheckExact(p))
	{
		size = PyBytes_Size(p);
		printf("size: %ld\n", size);
		printf("trying string: %s\n", PyBytes_AsString(p));
		size++;
		if (size > 10)
			size = 10;
		printf("first %ld bytes: ", size);
		holder = PyBytes_AsString(p);
		for (i = 0; i < size; i++)
		{
			if (i > 0)
				printf(" ");
			printf("%02x", (unsigned char)holder[i]);
		}
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");

}


void print_python_list(PyObject *p)
{
	Py_ssize_t size_p, allocated, idx = 0;
	PyObject *element;
	const char *type;

	printf("[*] Python list info\n");
	size_p = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size_p);
	printf("[*] Allocated = %ld\n", allocated);
	while (idx < size_p)
	{
		element = PyList_GET_ITEM(p, idx);
		type = element->ob_type->tp_name;
		printf("Element %ld: %s\n", idx, type);
		if (PyBytes_Check(element))
			print_python_bytes(element);
		idx++;
	}
}
