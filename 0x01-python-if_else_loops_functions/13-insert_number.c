#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current;
    listint_t *tail;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    new->n = number;

    current = *head;
    if (current == NULL)
        return (NULL);
    if (current->next == NULL)
    {
        new->next = current;
        new = *head;
    }
    if (new->n < current->n)
    {
        new->next = current;
        new = *head;
    }
    else
    {
        current = current->next;
        tail = *head;
        while (new->n > current->n)
        {
            current = current->next;
            tail = tail->next;
        }
        new->next = current;
        tail->next = new;
    }
    return (new);
}
