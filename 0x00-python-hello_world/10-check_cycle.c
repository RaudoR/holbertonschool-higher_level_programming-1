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
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = list->next;
	while (slow != NULL && fast->next != NULL && fast->next->next != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
