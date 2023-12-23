class ModelAdminForm(forms.ModelForm):
    def clean(self):
        # custom validation
        if self.instance is not None:
            pass

    class Meta:
        model = Model
        fields = "__all__"


class ModelAdmin(admin.ModelAdmin):
    actions = ("custom_action",)
    form = ModelAdminForm

    @admin.action(description="Custom action")
    def custom_action(self, request, queryset):
        updated = queryset.update(
            locked=True,
        )
        self.message_user(
            request,
            ngettext(
                singular=f"{updated} value updated",
                plural=f"{updated} values updated",
                number=updated,
            ),
            messages.SUCCESS,
        )
