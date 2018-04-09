#include "lists.h"

/**
 * check_cycle - check if the link list has a cycle
 *
 * @list: list of the linked list
 *
 * Return: 0 if there is no cylce 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *holder, *head;
	int n = 0, count = 0;

	if (list == NULL || list->next == NULL)
		return (0);
	head = list;
	while (list != NULL && list->next != NULL)
	{
		holder = head;
		n = 0;
		while (n < count)
		{
			if (holder == list)
				return (1);
			n++;
			holder = holder->next;
		}
		list = list->next;
		count++;
	}
	return (0);
}
