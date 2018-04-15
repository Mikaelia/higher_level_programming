#include "lists.h"
/**
  * add_dnodeint_end - adds a new node at the end of a dlistint_t list.
  * @head: head of linked list
  * @n: value of node
  * Return: pointer to head of list
  */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new;
	dlistint_t *temp;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
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
