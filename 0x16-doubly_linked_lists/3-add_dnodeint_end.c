#include "lists.h"

/**
  * add_dnodeint - adds a new node at the end  of a dlistint_t list.
  *
  * Return: Always EXIT_SUCCESS.
  */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new;
	dlistint_t *temp;

	if (head == NULL)
		return NULL;

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return NULL;
	new->n = n;
	if (*head == NULL)
	{
		new->next = NULL;
		new->prev = NULL;
		*head = new;
		return (*head);
	}

	temp = *head;

	while (temp->next != NULL)
	{
		temp = temp->next;
	}

	new->next = NULL;
	new->prev = temp;
	temp->next = new;
	return (*head);
}
