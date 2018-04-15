#include "lists.h"
/**
  * print_dlistint - prints the list and number of nodes
  * @h: pointer to head of list
  *
  * Return: number of nodes
  */
size_t print_dlistint(const dlistint_t *h)
{
	int count;

	count = 0;
	if (h == NULL)
		return (0);
	while (h != NULL)
	{
		count++;
		printf("%d\n", h->n);
		h = h->next;
	}
	return (count);
}
