#include "lists.h"
/**
  * dlistint_len - finds length of list
  * @h: pointer to the head of the list
  *
  * Return: number of nodes in the list
  */
size_t dlistint_len(const dlistint_t *h)
{
	int count;

	count = 0;
	if (h == NULL)
		return (0);
	while (h != NULL)
	{
		count++;
		h = h->next;
	}
	return (count);
}
