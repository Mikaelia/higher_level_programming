#include "lists.h"
/**
  * a function that deletes the node at index index of a dlistint_t linked list
  * index: The index of the node that should be deleted
  * Return: 1 if it succeeded, -1 if it failed
  */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	unsigned int count;
	dlistint_t *temp;
	dlistint_t *prev;
	dlistint_t *next;

	temp = *head;

	count = 0;
	if (head == NULL)
		return (-1);
	if (*head  == NULL)
	{
		return (-1);
	}
	if (index == 0 || *head == NULL)
	{
		temp = (*head)->next;
		*head = temp;
		return (1);

	}
	while (temp != NULL)
	{
		if (count == index)
		{
			prev = temp->prev;
			next = temp->next;
			prev->next = next;
			next->prev = prev;
			return (1);
		}
		count++;
		temp = temp->next;
	}
	return (-1);
}
