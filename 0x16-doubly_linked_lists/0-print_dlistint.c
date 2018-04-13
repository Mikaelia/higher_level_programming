#include "lists.h"
/**
  *
  *
  *
  *
  */
size_t print_dlistint(const dlistint_t *h)
{
	int count;
	count = 0;

	if (h == NULL)
		return(0);
	while (h != NULL)
	{
		count++;
		printf("%d\n", h->n);
		h = h->next;
	}
	return(count);
}
