function ScrollItemSubstance(baseElement)
{
    var self = this;

    //Construction
    {
        self.item = baseElement.clone();
        baseElement.remove();
    }

    self.getNewItem = function (data)
    {
        var item = self.item.clone();
        item.css("cursor", "pointer");
        item.find(".title").text(data.name);

        item.attr({
            "data-id":         data.id,
            "data-name":       data.name,
            "data-unit_id":    data.unit_id,
            "data-unit_label": data.unit_label
        });

        return item;
    };
}