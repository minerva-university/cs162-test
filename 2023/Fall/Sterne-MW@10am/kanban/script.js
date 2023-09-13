var kanban = {
  sortableKanbanCards: new Draggable.Sortable(document.querySelectorAll('.kanban-col .card-list-body'), {
    plugins: [SwapAnimation.default],
    draggable: '.card-list-item',
    handle: '.card-list-item',
    appendTo: 'body',
    cursor: "grabbing",
  })
};