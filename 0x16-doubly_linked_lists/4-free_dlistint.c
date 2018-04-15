#include "lists.h"
/**
  * free_dlistint - frees double linked list
  * @head: head of linked list
  *
  * Return: void
  */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *temp;

	while (head != NULL)
	{
		temp = head;
		head = head->next;
		free(temp);
	}
	free(head);
}
