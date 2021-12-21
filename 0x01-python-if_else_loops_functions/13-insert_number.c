#include "lists.h"
/**
 * insert_node - insert node in sort list
 *
 * @head: head of the linked lists
 * @number: number of the new node
 * Return: Address position to new node
 */
listint_t *insert_node(listint_t **head, int number)
{

	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		if (current->n == number)
		{
			free(new);
			return (NULL);
		}
		while ((current->next != NULL) && (current->next->n <= number))
		{

			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
