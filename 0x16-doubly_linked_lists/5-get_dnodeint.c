#include "lists.h"
/**
  * gets node at index
  *
  * Return: Address of the node, or NULL
  */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int count;

	count = 0;
	if (head == NULL)
		return (NULL);
	while(head != NULL)
	{
		if (count == index)
			return (head);
		else
		{
			count++;
			head = head->next;
		}
	}
	return (NULL);
}
