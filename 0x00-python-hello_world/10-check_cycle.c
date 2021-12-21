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

	if(list == NULL || list->next == NULL)
		return(0);

	while (list != NULL && list->next != NULL)
	{
		if (list->next == temp)
			return (1);
		list = list->next;
	}
	return (0);
}
