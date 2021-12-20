#include "lists.h"
/**
 * check_cycle - Check if linked list has cycle
 *
 * @list: entry list
 * Return: 1 if has a cycle 0 if hasn't
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	int i = 0;

	while (list != NULL)
	{
		if (list->next == temp)
			return (1);
		list = list->next;
		i++;
	}
	return (0);
}
