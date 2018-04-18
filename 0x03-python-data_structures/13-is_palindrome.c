#include "lists.h"

/**
 * reverse - reverse the list
 *
 * @head: input head address
 *
 * Return: reversed list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *holder = NULL;
	listint_t *next_h;

	if (*head == NULL)
		return (NULL);
	while (*head != NULL)
	{
		next_h = (*head)->next;
		(*head)->next = holder;
		holder = *head;
		*head = next_h;
	}
	*head = holder;
	return (*head);
}

/**
 * is_palindrome - check if the list is a palindrome
 *
 * @head: head of the list
 *
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *mid, *holder;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	else
	{
		fast = *head;
		slow = *head;
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;
		}
		if (fast == NULL)
			mid = slow;
		else
			mid = slow->next;
		mid = reverse(&mid);
		holder = *head;
		while (mid != NULL)
		{
			if (holder->n == mid->n)
			{
				holder = holder->next;
				mid = mid->next;
			}
			else
				return (0);
		}
		return (1);
	}
}
