#include "lists.h"
/**
 * print_dlistint - Prints all the elements of a dlistint_t list
 * @h: Doubly linked list
 *
 * Return: Number of node
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t n;

	while (h && h->next)
	{
		printf("%d\n", h);
		h = h->next;
		n++;
	}

	return (n);
}
