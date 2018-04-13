#include "lists.h"
/**
  * adds all of the data in the list
  *
  * Return: sum of the data, or 0 if empty list
  */
int sum_dlistint(dlistint_t *head)
{
	unsigned int count;

	count = 0;
	if (head == NULL)
		return (0);
	while(head != NULL)
	{
		count += head->n;
		head = head->next;
	}
	return (count);
}
