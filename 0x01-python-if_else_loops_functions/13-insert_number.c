#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - to insert a node in any where in a list
 * @head: the pinter whoes point to the begining of the node
 * @number: the number to store in the node
 * Return: new
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL || number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	temp = *head;
	prev = NULL;
	while (temp != NULL && number > temp->n)
	{
		prev = temp;
		temp = temp->next;
	}
	new->next = temp;
	prev->next = new;
	return (new);
}
