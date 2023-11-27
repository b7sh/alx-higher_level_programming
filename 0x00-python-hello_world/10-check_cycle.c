#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - chaeck if the singly linked list have a cycle in it
 * @list: the pointer to the node
 * Return: 0 if it fail or 1 in success
 */

int check_cycle(listint_t *list)
{
	listint_t *new, *find;

	if (list == NULL || list->next == NULL)
		return (0);

	new = list;
	find = list;

	while (find != NULL && find->next != NULL)
	{
		new = new->next;
		find = find->next->next;

		if (new == find)
			return (1);
	}
	return (0);
}
