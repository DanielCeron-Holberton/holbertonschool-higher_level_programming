#include <stdio.h>
#include <stdlib.h>
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
	int sum = 0;

	
	if (*head == NULL)
		return(0);
	
	current = *head;

	while (current->next != NULL)
	{
		if (current->n != current->next->n)
			sum += current->n;
		else
		{
			sum += current->n;
			break;
		}
		current = current->next;
	}

	while (current->next != NULL)
	{
		current = current->next;
		sum -= current->n;
	}
	if (sum == 0)
		return (1);
	else
		return(0);

	
	return (0);
}
