#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: parameter
 *
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
		
	return (is_reverce(head, *head));
}

/**
* is_reverce - func to reverce linked listint_t list.
* @head: parameter1
* @end: parameter2
*/

int is_reverce(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (is_reverce(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
