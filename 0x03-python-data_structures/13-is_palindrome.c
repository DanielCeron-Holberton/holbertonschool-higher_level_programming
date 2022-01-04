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
	listint_t *current, *temp;
	int sum[4096];
	int i = 0, size_array = 0, pair = 0;

	if (head == NULL || *head == NULL)
		return (1);
	current = *head;
	temp = *head;
	while (temp->next != NULL)
	{
		size_array++;
		temp = temp->next;
	}
	i = 0;
	while (current != NULL)
	{
		sum[i] = current->n;
		i++;
		current = current->next;
	}
	pair = (size_array / 2) + 1;
	if (size_array % 2 != 0)
	{
		for (i = 0; pair >= 0; i++, size_array--, pair--)
		{
			if (sum[i] != sum[size_array])
				return (0);
		}
	}
	else
	{
		while (i != size_array)
		{
			if (sum[i] != sum[size_array])
				return (0);
			i++, size_array--;
		}
	}
	return (1);
}
