#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_listint - reverse the list
 * @head: the pointer to the first node
 * Return: nothing
*/

void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}


int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *temp = *head, *reverse = NULL;
	if (*head == NULL || (*head)->next == NULL)
		return(1);
	while(1)
	{
		f = f->next->next;
		if (!f)
		{
			reverse = s->next;
			break;
		}
		if (!f->next)
		{
			reverse = s->next->next;
			break;
		}
	}
	reverse_listint(&reverse);

	while (reverse && temp)
	{
		if (temp->n == reverse->n)
		{
			reverse = reverse->next;
			temp = temp->next;
		}
		else
			return(0);
	}
	if (!reverse)
		return(1);
	return(0)
}
