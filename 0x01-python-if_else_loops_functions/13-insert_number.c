#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - that inserts a number into
 * a sorted singly linked list.
 * @head: parameter1
 * @number: parameter2
 *
 * Return: the address of the new node, or
 * NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (node == NULL || new->n < node->n)
	{
		new->next = node;
		*head = new;
		*head = new;
	}

	while (node)
	{
		if (!node->next || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
