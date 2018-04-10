#include "lists.h"

/**
 * insert_node - insterting a node in sorted linked list
 *
 * @head: head of the linked list
 *
 * @number: input integer to insert
 *
 * Return: linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *holder, *new;

	if (*head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	holder = *head;
	if (holder->n > number)
	{
		new->next = holder;
		*head = new;
		return (new);
	}
	else
		while (holder->next != NULL)
		{
			if (holder->n < number && holder->next->n > number)
			{
				new->next = holder->next;
				holder->next = new;
				return (new);
			}
			if (holder->n == number)
			{
				free(new);
				return (NULL);
			}
			holder = holder->next;
		}
	new->next = NULL;
	holder->next = new;
	return (new);
}
