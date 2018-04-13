#include "lists.h"

/**
  * main - check the code for Holberton School students.
  *
  * Return: Always EXIT_SUCCESS.
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
