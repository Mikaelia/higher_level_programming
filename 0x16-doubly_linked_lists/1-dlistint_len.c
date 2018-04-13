#include "lists.h"
/**
  *
  *
  *
  *
  */
size_t dlistint_len(const dlistint_t *h)
{
	int count;
	count = 0;

	if (h == NULL)
		return(0);
	while (h != NULL)
	{
		count++;
		h = h->next;
	}
	return(count);
}
