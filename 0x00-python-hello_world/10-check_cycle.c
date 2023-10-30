#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: parameter
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tur = list, *fas = list;

	if (list == NULL || list->next == NULL)
		return (0);
	tur = tur->next;
	fas = fas->next->next;

	while (tur && fas && hare->next)
	{
		if (tur == fas)
			return (1);
		tur = tur->next;
		fas = fas->next->next;
	}
	return (0);
}
