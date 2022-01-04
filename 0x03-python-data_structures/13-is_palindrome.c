#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * is_palindrome - Verify if the linked list is palindrome
 *
 * @head: Input linked list
 * Return: 1 if it's palindrome 0 if it's not
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int array_values[4096];
	int i = 0, pair = 0, j = 0;

	if (head == NULL || *head == NULL)
		return (1);
	current = *head;
	while (current)
	{
		array_values[i] = current->n;
		current = current->next;
		i++;
	}
	i--;
	pair = i / 2;
	for (j = 0; j <= pair; i--, j++)
	{
		if (array_values[i] != array_values[j])
			return (0);
	}
	return (1);
}
