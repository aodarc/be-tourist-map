import uuid


def upload_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<instance_class_name>/<filename>
    name = '{}.{}'.format(uuid.uuid4(), filename.split('.')[-1])
    return '{}/{0}/{1}'.format(instance.__class__.__name__,
                               instance.slider.pk,
                               name)
